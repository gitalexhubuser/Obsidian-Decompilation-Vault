---
offset: "0x0087ee60"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0087ee60 — `SE2_CreateWaveData`

- **Адрес (Offset):** `0x0087ee60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0087ee60
int32_t SE2::CreateWaveData(FMOD::System* system, const char* filename, FMOD_MODE mode, SESound* sound, FMOD::SoundGroup* loadSoundGroup, FMOD::SoundGroup* soundGroup, bool randomStart, int32_t priority, int32_t reverb, bool streaming, uint32_t decodeBufferSize, int32_t software, float coneInsideAngle, float coneOutsideAngle, float coneOutsideVolume, const C3Vector* coneOrientation) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0087ee60 в IDA Pro / Ghidra
