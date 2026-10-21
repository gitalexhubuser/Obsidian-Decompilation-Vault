---
offset: "0x00428f60"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Time/Win64/Time.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428f60 — `System_Time_MeasureDrift`

- **Адрес (Offset):** `0x00428f60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Time/Win64/Time.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428f60
double System_Time::MeasureDrift(int64_t frequency, LARGE_INTEGER* counter, DWORD* tickCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428f60 в IDA Pro / Ghidra
