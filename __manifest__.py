# ── FILE: product_account_autofill_js/__manifest__.py ────────────────────────
# Auto-fill account_id from product_id on account.move.line — pure JS (OWL).
# GitHub base: odoo/odoo account.move.line (_compute_account_id) [G]
# ─────────────────────────────────────────────────────────────────────────────
{
    "name": "Product → Account Auto-fill (JS only)",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "summary": "Fill accoufnt_id when product_id changes on Journal Items, client-side (no Python onchange).",
    "author": "It dev",
    "license": "LGPL-3",
    "depends": [
        "account",  # [G] account.move.line, product.product accounts live here
    ],
    # Odoo 17+ way to register front-end assets. The legacy
    # <template inherit_id="web.assets_backend"> XML approach still works but is
    # discouraged since v15 — the manifest dict below is the canonical method.
    "assets": {
        "web.assets_backend": [
            "product_account_autofill_js/static/src/js/move_line_account_autofill.js",
        ],
    },
    "installable": True,
    "application": True,
}
