---
offset: "0x00915a80"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00915a80 — `OutputWavWriter_getDriverNameCallback`

- **Адрес (Offset):** `0x00915a80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_wavwriter.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00915a80
FMOD_RESULT F_CALLBACK OutputWavWriter::getDriverNameCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00915a80 в IDA Pro / Ghidra
