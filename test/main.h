/******************************************************************************

 * 
 * 
(C) Copyright Pumpkin, Inc. All Rights Reserved.

This file may be distributed under the terms of the License
Agreement provided with this software.

THIS FILE IS PROVIDED AS IS WITH NO WARRANTY OF ANY KIND,
INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE.

$Source: C:\\RCS\\D\\Pumpkin\\CubeSatKit\\Example\\PIC24\\PIC24EP256MC206\\GPSRM1\\App\\App1\\main.h,v $
$Author: aek $
$Revision: 3.0 $
$Date: 2014-06-01 16:23:21-07 $

******************************************************************************/
#ifndef __main_h
#define __main_h

// define which module the project is for
//#define SUPMCU_BIM

// Symbols, etc.
#define STR_MODULE               "SIM"
#define STR_MODULE_APP           "SIM 1"
#define STR_MODULE_VERSION       "0.11.1a"
#if defined(SUPMCU_SIM1_REVA)
#define STR_HW_REVISION          "Rev A"
#elif defined(SUPMCU_SIM1_REVB)
#define STR_HW_REVISION          "Rev B"
#elif defined(SUPMCU_SIM1_REVC)
#define STR_HW_REVISION          "Rev C"
#endif
#define STR_DATE                __DATE__ " at " __TIME__
#define STR_BAUD_RATE         	"115200"
#define STR_1TAB              	"\t"
#define STR_2TABS             	"\t\t"
#define STR_CRLF              	"\r\n"
#define STR_STARTING   			"Starting..."
#define STR_FINISHED			"Finished."
#define STR_STOPPED			    "Stopped."

// Other macros.
#define LOOP_HERE()            	do { ; } while (1)

// I2C
#define I2C_ADDRESS				0x50

// CLI 
#define SUPMCU_ADDR             0x50
// Target-specific symbols.
#define SYSTEM_TIMER_RELOAD    	328
#define NOP                    	_NOP()

extern char strTmp[];

#define PRINTOUT uart1_msg_hhmmsstt(strTmp)


// MPLAB C30's lack of __enable_interrupt() is addressed here ...
#define __enable_interrupt()   do { __asm__ volatile("disi #0x0000"); } while (0)
#define __disable_interrupt()  do { __asm__ volatile("disi #0x3FFF"); } while (0)

#endif /* __main_h */
