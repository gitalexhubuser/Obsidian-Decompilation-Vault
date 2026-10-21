---
offset: "0x0052d410"
module: "WoW/Source"
file: "WoW/Source/Ui/PartyFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0052d410 — `CGPartyInfo_AddMember`

- **Адрес (Offset):** `0x0052d410`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/PartyFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0052d410
void CGPartyInfo::AddMember(WOWGUID guid, int32_t online, const CGPartyMemberState* state, uint8_t assignments, uint32_t role, const PartyReadyCheckInfo* readyCheck) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0052d410 в IDA Pro / Ghidra
