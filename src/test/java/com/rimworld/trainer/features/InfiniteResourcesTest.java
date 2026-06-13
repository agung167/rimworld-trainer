package com.rimworld.trainer.features;

import org.junit.Test;
import static org.junit.Assert.*;

public class InfiniteResourcesTest {
    @Test
    public void testEnableDisable() {
        InfiniteResources.enable();
        InfiniteResources.disable();
        assertTrue("InfiniteResources should handle enable/disable without exceptions", true);
    }
}