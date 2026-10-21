---
offset: "0x004e27c0"
module: "WoW/Source"
file: "WoW/Source/Glue/CharacterSelection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004e27c0 — `CCharacterSelection_GuildCallback`

- **Адрес (Offset):** `0x004e27c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/CharacterSelection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004e27c0
void CCharacterSelection::GuildCallback(int32_t guildID, const WOWGUID& guid, void* param, bool success) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004e27c0 в IDA Pro / Ghidra
