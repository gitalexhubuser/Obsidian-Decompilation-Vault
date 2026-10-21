---
offset: "0x0076c970"
module: "WoW/Common"
file: "WoW/Common/WowTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x0076c970 — `WowTime_WowDecodeTime`

- **Адрес (Offset):** `0x0076c970`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/WowTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0076c970
void WowTime::WowDecodeTime(uint32_t value, int32_t* minute, int32_t* hour, int32_t* weekDay, int32_t* monthDay, int32_t* month, int32_t* year, int32_t* flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0076c970 в IDA Pro / Ghidra
