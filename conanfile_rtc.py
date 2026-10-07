from conans import ConanFile


class VulkanMemoryAllocatorConan(ConanFile):
    name = "vulkan-memory-allocator"
    version = "3.4.0"
    url = "https://github.com/Esri/VulkanMemoryAllocator/blob/runtimecore"
    license = "https://github.com/Esri/VulkanMemoryAllocator/blob/runtimecore/LICENSE.txt"
    description = "Easy to integrate Vulkan memory allocation library."

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/include"
        relative = "3rdparty/VulkanMemoryAllocator/include"

        # headers
        self.copy("*.h*", src=base, dst=relative)
