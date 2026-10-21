---
offset: "0x00914d70"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00914d70 — `OutputNoSound_getDriverNameCallback`

- **Адрес (Offset):** `0x00914d70`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_output_nosound.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00914d70
FMOD_RESULT F_CALLBACK OutputNoSound::getDriverNameCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00914d70 в IDA Pro / Ghidra
