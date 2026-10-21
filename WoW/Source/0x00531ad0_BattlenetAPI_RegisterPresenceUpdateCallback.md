---
offset: "0x00531ad0"
module: "WoW/Source"
file: "WoW/Source/Ui/BattlenetAPI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00531ad0 — `BattlenetAPI_RegisterPresenceUpdateCallback`

- **Адрес (Offset):** `0x00531ad0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/BattlenetAPI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00531ad0
uint32_t BattlenetAPI::RegisterPresenceUpdateCallback(uint32_t presenceId, uint32_t field, GeneralFunction::Callback* callback) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00531ad0 в IDA Pro / Ghidra
