import unittest
from tools.log_analyzer import analyze

SHA="689b7385641e88b18b4eb6ca18dfad532499c860"
PACK={"source_commit":SHA,"rules":[{"id":"CHAT-L012","level":"INFO",
"logger_contains":"ZookeeperConfigLoader","message_contains":"Finished loading configuration from",
"source":"ZookeeperConfigLoader.java:84","proves":"completion log reached",
"does_not_prove":"all properties decrypted","hypotheses":["partial config"],
"next_checks":["check earlier decrypt WARN"]}]}

class LogPilotTests(unittest.TestCase):
    def test_version_gate(self):
        self.assertEqual(analyze([{}],PACK,"other")["status"],"VERSION_MISMATCH")
    def test_empty_logs(self):
        self.assertEqual(analyze([],PACK,SHA)["root_cause"],"UNKNOWN")
    def test_completion_not_success(self):
        x=analyze([{"level":"INFO","logger":"ZookeeperConfigLoader",
        "message":"Finished loading configuration from /x"}],PACK,SHA)
        self.assertEqual(x["matches"][0]["catalog_id"],"CHAT-L012")
        self.assertEqual(x["root_cause"],"UNKNOWN")
        self.assertIn("does_not_prove",x["matches"][0])
    def test_unmatched(self):
        self.assertEqual(analyze([{"level":"ERROR","logger":"x","message":"unseen"}],PACK,SHA)["matches"],[])
    def test_wrong_logger(self):
        self.assertEqual(analyze([{"level":"INFO","logger":"other","message":"Finished loading configuration from /x"}],PACK,SHA)["matches"],[])
    def test_invalid_event(self):
        with self.assertRaises(ValueError): analyze(["invalid"],PACK,SHA)

if __name__=="__main__": unittest.main()
