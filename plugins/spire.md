[yabridge compatibility tracker](../README.md) › Spire (Reveal Sound)

# Spire (Reveal Sound)

*Status: reported, mixed · last checked 2026-08-10*

[Vendor page](https://revealsound.com/)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Two reporters, two different walls, both to do with Direct3D and Direct2D rather
than with audio. Spire makes sound and responds to right-clicks; it is getting a
drawn interface that fails. Both reporters found a way through.

## Caveats and fixes

- Black window with Vulkan drivers installed: the reporter traced it to Wine's
  missing child-window rendering
  ([WineHQ bug 45277](https://bugs.winehq.org/show_bug.cgi?id=45277)) and worked
  around it by running Spire in a prefix whose `d3d9.dll`, `d3d10core.dll`,
  `d3d11.dll` and `dxgi.dll` come from a prefix *without* Vulkan support — symlink
  the rest of the prefix to save disk.
- 'error code 126: Module not found' on load means `d2d1.dll` is missing from the
  prefix. Install it and the plugin loads.
- Wine-tkg with the child-window patches did not work for one commenter: yabridge
  then failed with 'Application could not be started'.

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2024-03-21 | Black screen instead of the GUI once Vulkan drivers are installed; right-click menus and audio still work | Kubuntu 22.04, Bitwig Studio 4.4.10, WineHQ 9.0, yabridge 5.0.3, VST3 | [#318](https://github.com/robbert-vdh/yabridge/issues/318) (open, reported by gearcoded) |
| 2024-04-21 | Workaround: swap the Direct3D DLLs in the prefix for non-Vulkan ones | as above | [#318](https://github.com/robbert-vdh/yabridge/issues/318) (gearcoded) |
| 2023-12-29 | Fails to load with 'error code 126: Module not found'; resolved — the prefix needed `d2d1.dll` | Linux Mint 20, REAPER, Wine 7.9 Staging, VST2 and VST3 | [#296](https://github.com/robbert-vdh/yabridge/issues/296) (closed, reported by TheGuyWhoo) |

---

[Back to the tracker index](../README.md) · [How to correct this page](../CONTRIBUTING.md)
