# NOTES ON MODIFICATIONS.
# This is an ADDITION, not a replacement for the original file.
# The following code should be inserted AFTER the 'STRETCH' function (around line 115)
#


# Overlay if called
if [ "${OVER}" = "true" ] ; then
				# wx = ${CROP_WIDTH} * 0.5
				# hy = ${CROP_HEIGHT} * 0.5
        [ "${ALLSKY_DEBUG_LEVEL}" -ge 4 ] && echo "${ME}: Overlay for '${IMAGE_TO_USE}'"
        /home/pi/allsky/scripts/add_overlays_wrapper.sh ${IMAGE_TO_USE} ${IMAGE_TO_USE}
        if [ $? -ne 0 ] ; then
                echo -e "${RED}*** ${ME}: ERROR: OVERLAY failed; not saving{$NC}"
                exit 4
        fi
fi
