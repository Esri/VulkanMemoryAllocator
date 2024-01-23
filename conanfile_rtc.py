#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class VulkanMemoryAllocatorConan(ConanFile):
    name = "VulkanMemoryAllocator"
    version = "3.0.1"
    url = "https://github.com/Esri/VulkanMemoryAllocator/blob/runtimecore/LICENSE.txt"
    license = "https://github.com/Esri/VulkanMemoryAllocator/blob/runtimecore/LICENSE.txt"
    description = ("Easy to integrate Vulkan memory allocation library.")
    
    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/VulkanMemoryAllocator/"

        # headers
        self.copy("*.h*", src=base, dst=relative)
