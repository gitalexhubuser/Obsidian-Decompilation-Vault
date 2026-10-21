---
offset: "0x008cf800"
module: "WoW/Source"
file: "WoW/Source/WowServices/Grunt.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cf800 — `ClientLink_ClientLink`

- **Адрес (Offset):** `0x008cf800`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Grunt.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cf800
Grunt::ClientLink::ClientLink(Grunt::ClientResponse& clientResponse) : Grunt::Pending(18000), m_serverId(0), m_accountFlags(0), m_surveyId(0), m_localAddress(0), m_connection(nullptr), m_clientResponse(&clientResponse) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cf800 в IDA Pro / Ghidra
