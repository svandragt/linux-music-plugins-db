# ujam / Gorilla Engine / Loopcloud

*Status: verified · last checked 2026-08-10*

[Vendor page](https://www.ujam.com/) · [All plugins](../README.md)

*Second-hand reports, not a compatibility guarantee — nobody here retested this. Read the [caution](../README.md#read-this-first) before relying on it.*

Fail to load with a `JS_EXEC_FAILED` error until output redirection is turned off. Reported by several independent users.

## Caveats and fixes

- Enable the `disable_pipes` compatibility option for these plugins.
- Anything built on the Gorilla Engine is affected, not just ujam.
- Loopcloud vendor page: <https://www.loopcloud.com/>

## Findings

| Date | Report | Environment | Source |
| --- | --- | --- | --- |
| 2022-10-10 | Loopcloud Drum and Play doesn't work with `disable_pipes` true | unspecified | [#205](https://github.com/robbert-vdh/yabridge/issues/205) (closed, reported by Tabinol) |
| 2020-10-23 | Loopcloud unhandled exception | Bitwig 3.3 beta 3 | [#47](https://github.com/robbert-vdh/yabridge/issues/47) (closed, reported by plaimbock) |
| 2022-02-16 | 'Installation corrupted' error via yabridge but fine in Carla | unspecified | [#163](https://github.com/robbert-vdh/yabridge/issues/163) (closed, reported by TheGuyWhoo) |
| 2026-08-10 | `JS_EXEC_FAILED` and the `disable_pipes` fix | any host | [yabridge known issues](https://github.com/robbert-vdh/yabridge#known-issues-and-fixes) |
