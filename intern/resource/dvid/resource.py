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

from intern.resource import Resource
from abc import abstractmethod


class DvidResource(Resource):
    """Base class for Boss resources.

    Attributes:
        name (string): Name of resource.  Used as identifier when talking to
        the Boss API.
        description (string): Text description of resource.
        creator (string): Resource creator.
        raw (dictionary): Holds JSON data returned by the Boss API on a POST (create) or GET operation.
    """
    def __init__(self, name, description, creator='', raw={}):
        """Constructor.

        Args:
            name (string): Name of resource.
            description (string): Description of resource.
            creator (optional[string]): Resource creator.
            raw (optional[dictionary]): Holds JSON data returned by the Boss API on a POST (create) or GET operation.
        """

        self.name = name
        self.description = description
        self.creator = creator
        self.raw = raw

class CollectionResource(BossResource):
    """Top level container for Boss projects.
    """
    def __init__(
        self, name, description='', creator='', raw={}):
        """Constructor.

        Args:
            name (string): Collection name.
            description (optional[string]): Collection description.  Defaults to empty.
            creator (optional[string]): Resource creator.
            raw (optional[dictionary]): Holds JSON data returned by the Boss API on a POST (create) or GET operation.
        """
        BossResource.__init__(self, name, description, creator, raw)

    def get_route(self):
        return self.name

    def get_list_route(self):
        return ''

    def get_cutout_route(self):
        raise RuntimeError('Not supported for collections.')

    def get_reserve_route(self):
        raise RuntimeError('Not supported for collections.')

    def get_meta_route(self):
        return self.name

    def get_dict_route(self):
        return {"collection": self.name}


class ExperimentResource(BossResource):
    """Experiments reside inside a collection and contain channels and
    layers.

    Attributes:
        _coord_frame (string):
        num_hierarchy_levels (int):
        hierarchy_method (string):
        num_time_samples (int):
        time_step (int): Defaults to 0.
        time_step_unit (string): 'nanoseconds', 'microseconds', 'milliseconds', 'seconds'.  Defaults to 'seconds'.
    """
    def __init__(self, name, collection_name, coord_frame='', description='',
        num_hierarchy_levels=1, hierarchy_method='anisotropic',
        num_time_samples=1, creator='', raw={}, 
        time_step=0, time_step_unit='seconds'):
        """Constructor.

        Args:
            name (string): Experiment name.
            collection_name (string): Collection name.
            coord_frame (string): Name of coordinate frame used by experiment.  Defaults to empty.
            description (optional[string]): Experiment description.  Defaults to empty.
            num_hierarchy_levels (optional[int]): Defaults to 1.
            hierarchy_method (optional[string]): 'anisotropic', 'isotropic'  Defaults to 'anisotropic'.
            num_time_samples (optional[int]): Maximum number of time samples for any time series data captured by this experiment.  Defaults to 1.
            creator (optional[string]): Resource creator.
            raw (optional[dictionary]): Holds JSON data returned by the Boss API on a POST (create) or GET operation.
            time_step (optional[int]): Defaults to 0.
            time_step_unit (optional[string]): 'nanoseconds', 'microseconds', 'milliseconds', 'seconds'.  Defaults to 'seconds'.
        """

        BossResource.__init__(self, name, description, creator, raw)
        self.coll_name = collection_name

        self._valid_hierarchy_methods = ['anisotropic', 'isotropic']

        #ToDo: validate data types.
        self._coord_frame = coord_frame
        self.num_hierarchy_levels = num_hierarchy_levels
        self._hierarchy_method = self.validate_hierarchy_method(
            hierarchy_method)
        self.num_time_samples = num_time_samples

        self._valid_time_units = [
            '', 'nanoseconds', 'microseconds', 'milliseconds', 'seconds']
        self.time_step = time_step
        self._time_step_unit = self.validate_time_units(time_step_unit)





