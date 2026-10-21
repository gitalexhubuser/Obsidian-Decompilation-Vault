---
offset: "0x006277f0"
module: "WoW/Source"
file: "WoW/Source/UIUtil/Tooltip.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006277f0 — `CGTooltip_SetItem`

- **Адрес (Offset):** `0x006277f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/Tooltip.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006277f0
int32_t CGTooltip::SetItem(int32_t itemId, const WOWGUID* requester, const WOWGUID* itemGuid, int32_t nameOnly, int32_t compare, int32_t useLinkInfo, int32_t append, WOWGUID owner, int32_t socketPreview, FILE* stream, int32_t hideCharges, const ItemLinkInfo* link, int32_t minimumLevel, int32_t skipLock, int32_t skipSellPrice) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006277f0 в IDA Pro / Ghidra
