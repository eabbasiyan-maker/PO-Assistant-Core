"""Evidence-first source-pinned pilot. Sanitized input events only; no runtime access."""
import json
import argparse
from pathlib import Path

def analyze(events, pack, source_commit):
    if source_commit != pack["source_commit"]:
        return {"status":"VERSION_MISMATCH","root_cause":"UNKNOWN","matches":[],"next_checks":["Use the deployed build's matching product pack"]}
    if not isinstance(events, list) or not events:
        return {"status":"INSUFFICIENT_EVIDENCE","root_cause":"UNKNOWN","matches":[],"next_checks":["Provide sanitized runtime logs"]}
    matches=[]
    for index,event in enumerate(events):
        if not isinstance(event,dict):
            raise ValueError("Each event must be an object")
        candidates=[rule for rule in pack["rules"]
            if rule["level"] == str(event.get("level","")).upper()
            and rule["message_contains"] in str(event.get("message",""))
            and rule.get("logger_contains","") in str(event.get("logger",""))]
        if len(candidates)==1:
            r=candidates[0]
            matches.append({"event_index":index,"catalog_id":r["id"],"source":r["source"],
                            "proves":r["proves"],"does_not_prove":r["does_not_prove"],
                            "hypotheses":r.get("hypotheses",[]),"next_checks":r.get("next_checks",[])})
    return {"status":"PARTIAL_ANALYSIS" if matches else "INSUFFICIENT_EVIDENCE",
            "root_cause":"UNKNOWN","confidence":"SOURCE_MAPPING_ONLY" if matches else "NONE",
            "matches":matches,"unknown":["Runtime config and root cause not independently verified",
            "Unmatched/ambiguous events must not be classified by guesswork"],
            "next_checks":list(dict.fromkeys(x for m in matches for x in m["next_checks"]))}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--logs",required=True)
    p.add_argument("--pack",required=True)
    p.add_argument("--source-commit",required=True)
    a=p.parse_args()
    print(json.dumps(analyze(json.loads(Path(a.logs).read_text()),json.loads(Path(a.pack).read_text()),a.source_commit),indent=2))
