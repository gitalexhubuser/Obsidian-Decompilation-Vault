---
offset: "0x004d4850"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d4850 — `ExpirePendingHandlers`

- **Адрес (Offset):** `0x004d4850`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d4850
static void ExpirePendingHandlers(TSExplicitList<CMirrorHandler, offsetof(CMirrorHandler, m_link2)>* pending) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d4850 в IDA Pro / Ghidra
