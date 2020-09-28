# Copyright 2020 Aaron Webster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load("@rules_pkg//:pkg.bzl", "pkg_deb", "pkg_tar")

pkg_tar(
    name = "mode644_files",
    srcs = glob(["skel/mode644/**"]),
    mode = "0644",
    strip_prefix = "skel/mode644/",
)

pkg_tar(
    name = "mode755_files",
    srcs = glob(["skel/mode755/**"]),
    mode = "0755",
    strip_prefix = "skel/mode755/",
)

pkg_tar(
    name = "debian_data",
    extension = "tar.gz",
    deps = [
        ":mode644_files",
        ":mode755_files",
    ],
)

pkg_deb(
    name = "minecraft_server",
    data = ":debian_data",
    depends = [
        "libacl1-dev",
        "libssl-dev",
        "cython3",
        "python3-msgpack",
        "git",
        "ddclient",
        "python3-dbus",
    ],
    description = "Minecraft Server Files",
    homepage = "https://github.com/AaronWebster/minecraft",
    maintainer = "Aaron Webster",
    package = "minecraft-server",
    postinst = "postinst",
    version = "1.0.3",
)
