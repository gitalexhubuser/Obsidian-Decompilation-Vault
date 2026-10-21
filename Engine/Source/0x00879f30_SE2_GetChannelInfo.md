---
offset: "0x00879f30"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00879f30 — `SE2_GetChannelInfo`

- **Адрес (Offset):** `0x00879f30`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00879f30
int32_t SE2::GetChannelInfo(SEChannelInfo* info, int32_t maxCount, int32_t playing, int32_t isVirtual, int32_t loading, int32_t other, uint32_t* hardwareCount, uint32_t* softwareCount, uint32_t* virtualCount, uint32_t* loadingCount, uint32_t* otherCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00879f30 в IDA Pro / Ghidra
