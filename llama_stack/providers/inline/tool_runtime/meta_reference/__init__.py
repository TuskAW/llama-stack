# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from .config import MetaReferenceToolRuntimeConfig
from .meta_reference import MetaReferenceToolRuntimeImpl


async def get_provider_impl(config: MetaReferenceToolRuntimeConfig, _deps):
    impl = MetaReferenceToolRuntimeImpl(config)
    await impl.initialize()
    return impl
