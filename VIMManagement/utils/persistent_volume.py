# All Rights Reserved.
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from VIMManagement.utils.kubernetes_api import KubernetesApi
from os_ma_nfvo.settings import VOLUME_PATH


class PersistentVolumeClient(KubernetesApi):
    def __init__(self, *args, **kwargs):
        if 'storage_size' in kwargs:
            self.storage_size = kwargs['storage_size']
        super().__init__(*args, **kwargs)

    def read_resource(self, **kwargs):
        return self.core_v1.read_persistent_volume(self.instance_name)

    def create_resource(self, **kwargs):
        self.core_v1.create_persistent_volume(self.resource)

    def patch_resource(self, **kwargs):
        self.core_v1.patch_persistent_volume(self.instance_name, self.resource)

    def delete_resource(self, **kwargs):
        self.core_v1.delete_persistent_volume(
            name=self.instance_name, body=self.delete_options)

    def instance_specific_resource(self, **kwargs):
        persistent_volume = self.kubernetes_client.V1PersistentVolume(
            api_version='v1', kind='PersistentVolume')
        persistent_volume.metadata = self.kubernetes_client.V1ObjectMeta(
            name=self.instance_name, labels={"name": self.instance_name})
        persistent_volume.spec = self.kubernetes_client.V1PersistentVolumeSpec(
            capacity={"storage": self.storage_size}, access_modes=["ReadWriteOnce"],
            host_path=self.kubernetes_client.V1HostPathVolumeSource(
                path='{}{}'.format(VOLUME_PATH, self.instance_name)))
        return persistent_volume
