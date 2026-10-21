---
offset: "0x0087f7a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087f7a0 — `SESound_Create2D`

- **Адрес (Offset):** `0x0087f7a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087f7a0
int32_t SESound::Create2D(const char* filename, int32_t looping, FMOD::SoundGroup* loadSoundGroup, FMOD::SoundGroup* soundGroup, bool randomStart, bool streaming, int32_t reverb, int32_t priority, uint32_t decodeBufferSize) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087f7a0 в IDA Pro / Ghidra
