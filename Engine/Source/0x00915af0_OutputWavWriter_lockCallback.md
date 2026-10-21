---
offset: "0x00915af0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00915af0 — `OutputWavWriter_lockCallback`

- **Адрес (Offset):** `0x00915af0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00915af0
FMOD_RESULT F_CALLBACK OutputWavWriter::lockCallback(FMOD_OUTPUT_STATE *output, unsigned int offset, unsigned int length, void **ptr1, void **ptr2, unsigned int *len1, unsigned int *len2)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00915af0 в IDA Pro / Ghidra
