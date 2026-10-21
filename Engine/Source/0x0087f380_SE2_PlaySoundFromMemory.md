---
offset: "0x0087f380"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087f380 — `SE2_PlaySoundFromMemory`

- **Адрес (Offset):** `0x0087f380`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087f380
void SE2::PlaySoundFromMemory(FMOD::System* system, const char* data, uint32_t length, FMOD_MODE mode, SESound* sound) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087f380 в IDA Pro / Ghidra
