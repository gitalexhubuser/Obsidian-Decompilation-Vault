---
offset: "0x005a47d0"
module: "WoW/Source"
file: "WoW/Source/Ui/GuildBankFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005a47d0 — `Signal_EVENT_GUILDBANKLOG_UPDATE`

- **Адрес (Offset):** `0x005a47d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GuildBankFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005a47d0
static void Signal_EVENT_GUILDBANKLOG_UPDATE(int32_t id, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005a47d0 в IDA Pro / Ghidra
