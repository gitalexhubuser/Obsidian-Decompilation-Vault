---
offset: "0x0047c110"
module: "Engine/Source"
file: "Engine/Source/Base/Status.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047c110 — `CStatus_GetErrorStr`

- **Адрес (Offset):** `0x0047c110`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Base/Status.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047c110
char* CStatus::GetErrorStr(char* buffer, size_t bufchars, STATUS_TYPE minSeverity, const char* separator) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047c110 в IDA Pro / Ghidra
