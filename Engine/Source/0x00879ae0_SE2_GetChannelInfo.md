---
offset: "0x00879ae0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/SoundEngine.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00879ae0 — `SE2_GetChannelInfo`

- **Адрес (Offset):** `0x00879ae0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/SoundEngine.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00879ae0
int32_t SE2::GetChannelInfo(bool fadingOnly, SEChannelInfo* info, int32_t maxCount, int32_t playing, int32_t isVirtual, int32_t loading, int32_t other, uint32_t* hardwareCount, uint32_t* softwareCount, uint32_t* virtualCount, uint32_t* loadingCount, uint32_t* otherCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00879ae0 в IDA Pro / Ghidra
