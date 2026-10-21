---
offset: "0x00572490"
module: "WoW/Source"
file: "WoW/Source/Ui/RaidInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00572490 — `RaidMemberRemovedNameCallback`

- **Адрес (Offset):** `0x00572490`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/RaidInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00572490
static void RaidMemberRemovedNameCallback(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00572490 в IDA Pro / Ghidra
