package com.rimworld.trainer.features;

import org.junit.Test;
import static org.junit.Assert.*;

public class GodModeTest {
    @Test
    public void testEnableDisable() {
        GodMode.enable();
        GodMode.disable();
        assertTrue("GodMode should handle enable/disable without exceptions", true);
    }
}