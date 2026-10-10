import unittest
from tools.log_analyzer import analyze

SHA = "689b7385641e88b18b4eb6ca18dfad532499c860"
PACK = {"source_commit": SHA, "rules": [
    {"id": "CHAT-L012", "level": "INFO", "logger_contains": "ZookeeperConfigLoader",
     "message_contains": "Finished loading configuration from",
     "source": "ZookeeperConfigLoader.java:84", "proves": "syncConfig reached completion logging",
     "does_not_prove": "all encrypted properties decrypted",
     "hypotheses": ["decryption may have failed for a property"],
     "next_checks": ["inspect preceding decryption warnings"]},
    {"id": "CHAT-L011", "level": "WARN", "logger_contains": "ZookeeperConfigLoader",
     "message_contains": "An exception occurred while trying to decrypt value of",
     "source": "ZookeeperConfigLoader.java:77", "proves": "decryption exception caught",
     "does_not_prove": "whole config load aborted",
     "hypotheses": ["property may remain encrypted"], "next_checks": ["check downstream property use"]},
    {"id": "CHAT-L013", "level": "INFO", "logger_contains": "MessageQueueUtil",
     "message_contains": "Connected to ", "source": "MessageQueueUtil.java:60",
     "proves": "producerConnection.start returned",
     "does_not_prove": "producer and readers ready",
     "hypotheses": ["subsequent queue setup may fail"],
     "next_checks": ["inspect later JMSException and readers"]},
    {"id": "CHAT-L008", "level": "WARN", "logger_contains": "AsyncAdaptor",
     "message_contains": "An exception occurred in login_onResult. error code=",
     "source": "AsyncAdaptor.java:224", "proves": "ChatException caught",
     "does_not_prove": "specific operation that threw",
     "hypotheses": ["authorization or dispatch path may have failed"],
     "next_checks": ["correlate uniqueId with surrounding events"]}
]}

class IntegrationTests(unittest.TestCase):
    def test_decrypt_then_completion(self):
        result = analyze([
            {"level": "WARN", "logger": "ZookeeperConfigLoader", "message": "An exception occurred while trying to decrypt value of key"},
            {"level": "INFO", "logger": "ZookeeperConfigLoader", "message": "Finished loading configuration from /path"}
        ], PACK, SHA)
        self.assertEqual([m["catalog_id"] for m in result["matches"]], ["CHAT-L011", "CHAT-L012"])
        self.assertEqual(result["root_cause"], "UNKNOWN")

    def test_queue_not_ready(self):
        result = analyze([{"level": "INFO", "logger": "MessageQueueUtil", "message": "Connected to tcp://localhost:1"}], PACK, SHA)
        self.assertEqual(result["matches"][0]["does_not_prove"], "producer and readers ready")
        self.assertEqual(result["root_cause"], "UNKNOWN")

    def test_async_exception(self):
        result = analyze([{"level": "WARN", "logger": "AsyncAdaptor", "message": "An exception occurred in login_onResult. error code= 2 uniqueId= abc"}], PACK, SHA)
        self.assertEqual(result["matches"][0]["catalog_id"], "CHAT-L008")

    def test_wrong_version(self):
        self.assertEqual(analyze([{"level": "INFO", "logger": "MessageQueueUtil", "message": "Connected to foo"}], PACK, "different")["status"], "VERSION_MISMATCH")

    def test_ambiguous_rule_suppressed(self):
        duplicate_pack = dict(PACK)
        duplicate_pack["rules"] = PACK["rules"] + [dict(PACK["rules"][0])]
        result = analyze([{"level": "INFO", "logger": "ZookeeperConfigLoader", "message": "Finished loading configuration from /x"}], duplicate_pack, SHA)
        self.assertEqual(result["matches"], [])

    def test_unmatched_events_not_reported(self):
        result = analyze([{"level": "ERROR", "logger": "X", "message": "nothing"}], PACK, SHA)
        self.assertEqual(result["status"], "INSUFFICIENT_EVIDENCE")

if __name__ == "__main__":
    unittest.main()
