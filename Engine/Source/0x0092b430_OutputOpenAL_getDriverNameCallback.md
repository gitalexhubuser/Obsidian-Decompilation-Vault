---
offset: "0x0092b430"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0092b430 — `OutputOpenAL_getDriverNameCallback`

- **Адрес (Offset):** `0x0092b430`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/win32/src/fmod_output_openal.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0092b430
FMOD_RESULT F_CALLBACK OutputOpenAL::getDriverNameCallback(FMOD_OUTPUT_STATE *output, int id, char *name, int namelen)
```

## Исследование и заметки
- [ ] Открыть адрес 0x0092b430 в IDA Pro / Ghidra
