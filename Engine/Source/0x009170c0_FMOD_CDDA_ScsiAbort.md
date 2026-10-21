---
offset: "0x009170c0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009170c0 — `FMOD_CDDA_ScsiAbort`

- **Адрес (Offset):** `0x009170c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_os_cdda.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009170c0
bool FMOD_CDDA_ScsiAbort(SRB_ExecSCSICmd *srb_to_abort, unsigned char adapter_id)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009170c0 в IDA Pro / Ghidra
