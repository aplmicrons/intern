"""
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
"""
from intern.remote import Remote
from intern.resource.dvid.resource import *
from intern.service.dvid.service import *

LATEST_VERSION = 'v0'
CONFIG_PROTOCOL = 'protocol'
CONFIG_HOST = 'host'
api = ""


class DVIDRemote(Remote):

	def __init__(self, specs, version=None):
		"""
			Constructor.

			Checks for latest version. If no version is given, assigns version as none
			Protocol and host specifications are taken in as keys -values of dictionary.
			global api variable is named and used for every command that requires api.
		"""

		if version is None:
			version = LATEST_VERSION

		protocol = specs[CONFIG_HOST]
		host = specs[CONFIG_PROTOCOL]


		global api
		api = host + "://" + protocol
		

	def get_channel(self, ID, repos):
		"""
			Method to initialize the Project Service from the config data

			Args:
				version (string): Version of Boss API to use.

			Returns:
				None

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.get_channel(ID,repos)

	def get_cutout(self, IDrepos, xspan, yspan, zspan):
		"""
			Method to initialize the Project Service from the config data

			Args:
				version (string): Version of Boss API to use.

			Returns:
				None

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.get_cutout(api,IDrepos,xspan,yspan,zspan)


	def create_project(self, typename,dataname,version=0):
		"""
			Method to initialize the Project Service from the config data

			Args:
				version (string): Version of Boss API to use.

			Returns:
				None

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.create_project(api,typename,dataname,version)

	def create_cutout(self,UUID,typename,dataname,version=0):
		"""
			Method to initialize the Project Service from the config data

			Args:
				version (string): Version of Boss API to use.

			Returns:
				None

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.create_cutout(api,typename,dataname,version)

	def get_info(self, UUID):
		"""
			Method to initialize the Project Service from the config data

			Args:
				version (string): Version of Boss API to use.

			Returns:
				None

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidService.get_info(api,UUID)

	def get_log(self, UUID):
		"""
		Method to initialize the Project Service from the config data

		Args:
		    version (string): Version of Boss API to use.

		Returns:
		    None

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.get_log(api,UUID)

	def post_log(self, UUID,log1):
		"""
		Method to initialize the Project Service from the config data

		Args:
		    version (string): Version of Boss API to use.

		Returns:
		    None

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.post_log(api,UUID,log1)

	def get_server_info(self):
		"""
		Method to initialize the Project Service from the config data

		Args:
		    version (string): Version of Boss API to use.

		Returns:
		    None

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.get_server_info(api)

	def change_server_setting(self,gc1,throt1):
		"""
		Method to initialize the Project Service from the config data

		Args:
		    version (string): Version of Boss API to use.

		Returns:
		    None

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.change_server_setting(api,gc1,throt1)
		