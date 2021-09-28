# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from attachments_on_nextcloud.nextcloud import save_to_nextcloud

__version__ = '0.0.1'


@frappe.whitelist()
def migrate_to_nextcloud():
	files = frappe.get_list('File')
	for f in files:
		doc = frappe.get_doc('File', f.name)
		frappe.enqueue('attachments_on_nextcloud.nextcloud.save_to_nextcloud', doc=doc)