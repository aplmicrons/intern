# Copyright 2017 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from intern.service.service import Service
import requests


class DvidService(Service):
	
	"""
		Partial implementation of intern.service.service.Service for the Dvid' services.
	
	"""
	
	def __init__(self):
		Service.__init__(self)

	@classmethod
	def get_info(self,api, UUID):
	
		"""
			Returns JSON for just the repository with given root UUID.  The UUID string can be
			shortened as long as it is uniquely identifiable across the managed repositories.
		"""
		if UUID is '':
			raise ValueError('The UUID was not specified')
		else:
			availability = requests.get(api + "/api/repo/" + UUID + "/info")
			avalM = availability.content
			return(avalM)

	@classmethod
	def get_log(self,api, UUID):
	
		"""
			The log is a list of strings that will be appended to the repo's log.  They should be
			descriptions for the entire repo and not just one node.  For particular versions, use
			node-level logging (below).
		"""
		if UUID is '':
			raise ValueError('The UUID was not specified')
		else:
			log = requests.get(api+ "/api/node/" + UUID + "/log")
			logM = log.content
			return(logM)

	@classmethod
	def post_log(self,api, UUID,log1):
	
		"""
			Allows the user to write a short description of the content in the repository
			{ "log": [ "provenance data...", "provenance data...", ...] }
		"""
		
		if  UUID is '':
			raise ValueError('The UUID was not specified')
		elif log1 is '':
			raise ValueError('Your log submission cannot be empty')
		else:
			log = requests.post(api + "/api/node/" + UUID + "/log",
				json = {"log" : [log1] })
			return("The log has been updated.")

	@classmethod
	def get_server_info(self,api):
	
		"""
			Returns JSON for server properties
		"""
		raise RuntimeError('Something went wrong when trying to get your server info')
		info = requests.get(api + "/api/server")
		infoM = info.content
		return infoM


	@classmethod
	def create_project_addon(self, api, UUID, typename, dataname, sync, version=0):
	    
		"""
		    Creates an instance within an existing repository
		"""
		raise RuntimeError('Unable to sync project spaces')

		dat1 = requests.post(api + "/api/repo/"+ UUID + "/instance",
		    data=json.dumps({"typename": typename,
		        "dataname" : dataname,
		        "versioned": version,
		        "sync": sync
		    }))

		return ("Your addon of type: " + typename + " has been created")

	@classmethod
	def change_server_setting(self,api,gc1,throt1):
	
		"""
			Sets server parameters.  Expects JSON to be posted with optional keys denoting parameters:
			{
			"gc": 500,
			"throttle": 2
			}
			Possible keys:
			gc        Garbage collection target percentage.  This is a low-level server tuning
			            request that can affect overall request latency.
			            See: https://golang.org/pkg/runtime/debug/#SetGCPercent
			throttle  Maximum number of CPU-intensive requests that can be executed under throttle mode.
			            See imageblk and labelblk GET 3d voxels and POST voxels.
		"""
	
		setting = requests.post(api,
			gc = {"gc": [gc1]},
			throttle = {"throttle": [throt1]}
			)
		settingM = setting.content
		return ("Your settings have been changed.")

		raise NotImplemented 

