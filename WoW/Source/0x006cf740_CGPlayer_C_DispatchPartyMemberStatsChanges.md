---
offset: "0x006cf740"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Player_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006cf740 — `CGPlayer_C_DispatchPartyMemberStatsChanges`

- **Адрес (Offset):** `0x006cf740`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Player_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006cf740
void CGPlayer_C::DispatchPartyMemberStatsChanges(const WOWGUID& guid, uint32_t changes, const CGPartyMemberState* oldState, const CGPartyMemberState* newState) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006cf740 в IDA Pro / Ghidra
