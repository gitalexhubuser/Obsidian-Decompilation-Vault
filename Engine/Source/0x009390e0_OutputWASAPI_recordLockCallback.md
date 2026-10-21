---
offset: "0x009390e0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x009390e0 — `OutputWASAPI_recordLockCallback`

- **Адрес (Offset):** `0x009390e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_wasapi.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009390e0
FMOD_RESULT F_CALLBACK OutputWASAPI::recordLockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x009390e0 в IDA Pro / Ghidra
