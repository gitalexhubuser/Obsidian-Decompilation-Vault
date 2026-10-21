---
offset: "0x00465550"
module: "WoW/Source"
file: "WoW/Source/WowServices/Login.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00465550 — `Login_GetFileStatus`

- **Адрес (Offset):** `0x00465550`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Login.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00465550
void Login::GetFileStatus(const char* fileName, uint64_t size, const uint8_t* md5) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00465550 в IDA Pro / Ghidra
