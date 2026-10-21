---
offset: "0x00574f10"
module: "WoW/Source"
file: "WoW/Source/Ui/RaidInfo.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00574f10 — `CGRaidInfo_UpdateRoster`

- **Адрес (Offset):** `0x00574f10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/RaidInfo.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00574f10
void CGRaidInfo::UpdateRoster(const WOWGUID* guids, const uint32_t* subgroups, const uint8_t* flags, const uint32_t* roles, const uint8_t* online, uint32_t count, uint8_t battleground) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00574f10 в IDA Pro / Ghidra
