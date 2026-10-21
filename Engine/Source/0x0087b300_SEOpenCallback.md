---
offset: "0x0087b300"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087b300 — `SEOpenCallback`

- **Адрес (Offset):** `0x0087b300`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087b300
static FMOD_RESULT F_CALLBACK SEOpenCallback(const char* name, int unicode, unsigned int* filesize, void** handle, void** userdata) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087b300 в IDA Pro / Ghidra
