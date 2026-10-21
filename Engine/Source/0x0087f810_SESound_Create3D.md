---
offset: "0x0087f810"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087f810 — `SESound_Create3D`

- **Адрес (Offset):** `0x0087f810`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087f810
int32_t SESound::Create3D(const char* filename, int32_t looping, FMOD::SoundGroup* loadSoundGroup, FMOD::SoundGroup* soundGroup, bool randomStart, bool streaming, int32_t priority, int32_t software, float coneInsideAngle, float coneOutsideAngle, float coneOutsideVolume, const C3Vector* coneOrientation) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087f810 в IDA Pro / Ghidra
