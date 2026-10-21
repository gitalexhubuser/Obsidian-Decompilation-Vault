---
offset: "0x005fd1d0"
module: "WoW/Source"
file: "WoW/Source/UIUtil/InputControl.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005fd1d0 — `CGInputControl_CGInputControl`

- **Адрес (Offset):** `0x005fd1d0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/UIUtil/InputControl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005fd1d0
CGInputControl::CGInputControl() : m_flags(INPUT_NONE), m_lookStartTime(0), m_pendingDefaultAction(PENDING_ACTION_NONE), m_facingOverrideActive(0), m_facingOverride(0.0f), m_vehicleAimValid(0), m_vehicleAim(0.0f), m_mouseModeFlags(3), m_forceCursorOn(0), m_joystickMouseFlags(3), m_joystickLookX(0.0f), m_joystickLookY(0.0f), m_wowMouse(nullptr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005fd1d0 в IDA Pro / Ghidra
