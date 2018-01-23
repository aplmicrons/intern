# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
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

from intern.service import Service
import h5py

class MetadataService(Service):
    """MetadataService routes calls to the appropriate API version.
    """

    def __init__(self):
        """
            Constructor.
        """
        service.__init__(self)

    def create(self, resource, keys_vals):
        """Create the given key-value pairs for the given resource.

        Will attempt to create all key-value pairs even if a failure is encountered.

        Args:
            resource (intern.resource.boss.BossResource): List keys associated with this resource.
            keys_vals (dictionary): The metadata to associate with the resource.

        Raises:
            HTTPErrorList on failure.
        """
        i = 0
        keyN = len(keys_vals.keys())
        while i < keyN:
            key = keys_vals.keys()[i]
            value = keys_vals.values()[i]
            resource.__setitem__(key,value)
            i = i+1
        return 'Done creating metadata'

    def get(self, resource, keys):
        """Get metadata key-value pairs associated with the given resource.

        Args:
            resource (intern.resource.boss.BossResource): Get key-value pairs associated with this resource.
            keys (list): Keys to retrieve.

        Returns:
            (dictionary): The requested metadata for the given resource.

        Raises:
            HTTPErrorList on failure.
        """
        i = 0
        keyN = len(keys)
        output = [0]*keyN
        while i < keyN:
            key = keys[i]
            meta = resource.__getitem__(key)
            output[i] = meta
            i = i+1
        return output

    def update(self, resource, keys_vals):
        """Update the given key-value pairs for the given resource.

        Keys must already exist before they may be updated.  Will attempt to
        update all key-value pairs even if a failure is encountered.

        Args:
            resource (intern.resource.boss.BossResource): Update values associated with this resource.
            keys_vals (dictionary): The metadata to update for the resource.

        Raises:
            HTTPErrorList on failure.
        """
        i = 0
        keyN = len(keys_vals.keys())
        while i < keyN:
            key = keys_vals.keys()[i]
            value = keys_vals.values()[i]
            resource.__setitem__(key,value)
            i = i+1
        print 'Done updating metadata.'

    def delete(self, resource, keys):
        """Delete metadata key-value pairs associated with the given resource.

        Will attempt to delete all given key-value pairs even if a failure
        occurs.

        Args:
            resource (intern.resource.boss.BossResource): Delete key-value pairs associated with this resource.
            keys (list): Keys to delete.

        Raises:
            HTTPErrorList on failure.
        """
        i = 0
        keyN = len(keys_vals.keys())
        while i < keyN:
            key = keys_vals.keys()[i]
            value = keys_vals.values()[i]
            resource.__delitem__(key,value)
            i = i+1
        return 'Done deleting.'