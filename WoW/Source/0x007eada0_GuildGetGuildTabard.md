---
offset: "0x007eada0"
module: "WoW/Source"
file: "WoW/Source/Game/GameClient/CDrawBowString.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007eada0 — `GuildGetGuildTabard`

- **Адрес (Offset):** `0x007eada0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/GameClient/CDrawBowString.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007eada0
bool GuildGetGuildTabard(WOWGUID guid, int32_t guildID, void (*callback)(int32_t guildID, const WOWGUID& guid, void* param, bool success), void* param, int32_t& emblemStyle, int32_t& emblemColor, int32_t& borderStyle, int32_t& borderColor, int32_t& background) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007eada0 в IDA Pro / Ghidra
