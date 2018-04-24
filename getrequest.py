# -*- coding: utf-8 -*-
# @Author: chanshub
# @Date:   2018-01-29 23:02:11
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2018-02-24 00:35:14


import requests
import arrow
import argparse

BASE_URL = 'https://review-api.udacity.com/api/v1'
SUBMISSION_REQUEST = '{}/me/submission_requests.json'.format(BASE_URL)

def getHeader(token): return {'Authorization': token, 'Content-Length': '0'}

def submission_request(headers):
	try:
		time_fields = ["created_at", "updated_at", "closed_at"]
		for request in sorted([r for r in requests.get(SUBMISSION_REQUEST, headers=headers).json()], key=lambda r: r["id"], reverse=True):
			print(request["id"])
			for time_field in time_fields:
				when = arrow.get(request[time_field]).to('local')
				print("\t{}   {}".format(when.format("YYYY-MM-DD HH:mm"), when.humanize()))
	except Exception as e:
		print("Exception from submission_request()", str(e))

if __name__ == '__main__':
	cmd_parser = argparse.ArgumentParser(description =
		"Poll the Udacity reviews API to get details of maximum 5 submission requests."
	)
	cmd_parser.add_argument('--auth-token', '-T', dest='token',
		metavar='TOKEN', type=str, required=True,
		help="""Your Udacity auth token."""
	)
	args = cmd_parser.parse_args()
	
	headers = getHeader(args.token)
	submission_request(headers)


