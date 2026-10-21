---
offset: "0x0076c910"
module: "WoW/Common"
file: "WoW/Common/WowTime.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x0076c910 — `WowTime_WowEncodeTime`

- **Адрес (Offset):** `0x0076c910`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/WowTime.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0076c910
void WowTime::WowEncodeTime(uint32_t& value, int32_t minute, int32_t hour, int32_t weekDay, int32_t monthDay, int32_t month, int32_t year, int32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0076c910 в IDA Pro / Ghidra
