# -*- coding: utf-8 -*-
"""Visa CE 3.0 Compelling Evidence Pack Compiler for GenPark Agentic Commerce."""
import json
from typing import Dict, Any, List

class VisaCE30CompellingEvidencePackCompiler:
    @staticmethod
    def match_ce30_qualifying_historical_transactions(disputed_transaction: Dict[str, Any], customer_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        disp_ip = disputed_transaction.get("device_ip")
        disp_device = disputed_transaction.get("device_fingerprint")
        
        matches = []
        for tx in customer_history:
            if tx.get("age_days", 0) >= 120 and not tx.get("is_disputed", False):
                if (disp_ip and tx.get("device_ip") == disp_ip) or (disp_device and tx.get("device_fingerprint") == disp_device):
                    matches.append(tx.get("transaction_id"))
                    
        qualified = len(matches) >= 2
        return {
            "disputed_tx_id": disputed_transaction.get("transaction_id"),
            "qualifying_historical_matches": matches[:2],
            "ce30_criteria_met": qualified,
            "liability_shift_verdict": "AUTOMATIC_MERCHANT_WIN_LIABILITY_SHIFT" if qualified else "INSUFFICIENT_HISTORICAL_TRANSACTIONS",
            "statutory_basis": "Visa Core Rules and Visa Product and Service Rules, Section 10.4 (Compelling Evidence 3.0)"
        }

    @staticmethod
    def generate_ce30_vrol_pre_arbitration_packet(case_id: str, qualifying_tx_ids: List[str], shared_identifier_type: str = "device_fingerprint_and_ip") -> Dict[str, Any]:
        return {
            "vrol_case_id": case_id,
            "submission_protocol": "Visa Resolve Online (VROL) Pre-Arbitration",
            "evidence_class": "CE_3.0_RULE_10_4",
            "qualifying_prior_transactions": qualifying_tx_ids,
            "shared_identifier_proven": shared_identifier_type,
            "issuer_directive": "Reversal of chargeback with zero merchant dispute fee liability."
        }
