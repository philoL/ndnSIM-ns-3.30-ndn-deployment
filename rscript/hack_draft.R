setwd("/home/klaus/backup_ccn/ndnSIM-ns-3.30-ndn-deployment/rscript")

### Other Libraries ### 
suppressMessages(library(tidyverse))
library(magrittr, warn.conflicts = F)
library(gridExtra, warn.conflicts = F)
library(zoo, warn.conflicts = F) # For rolling mean.


# theme_set(theme_bw(base_size = 12, base_family = "CM Sans"))
theme_set(theme_bw() + theme( strip.background=element_blank(), 
	legend.key = element_rect(color="white"),
	panel.background=element_blank(), 
	panel.border=element_blank(), axis.line = element_line(size=0.3)) + 
		theme(legend.title=element_blank()))

folder <- str_c("../results/")

# Read in Data:
# cwnd = as_tibble(read.csv(sep=c('\t', ' '),"cwnd.txt"))
rates <- suppressMessages(read_tsv(str_c(folder,"rates.txt"), guess_max = 200000))
delay <- suppressMessages(read_tsv(str_c(folder,"delay.txt")))
drop <- suppressMessages(read_tsv(str_c(folder,"drop.txt")))

rates %<>%
	filter(Node == N0)
	# group_by(Time, Node) %>% 
	# mutate(KbSum = sum(Kilobytes), CompSum = 10000.0 / KbSum, UtilSum= -1.0/(KbSum*8/1024))

rates   %>% filter(Node == "N0", Type=="InData" )

(g.rates <- rates %>% filter(Node == "N0", Type=="OutData", FaceId==258 ) %>%
		ggplot(aes (x=Time, y=(Kilobytes*8)/1024, color=FaceId)) +
		geom_line(size=0.8) + 
		# geom_line(aes(y=KbSum*8/1024), size=0.8) +
		ylab("Rate [Mbps]") +
		ggtitle("Application Rate") +
		theme(legend.position="none") +
		expand_limits(y=0) +
		facet_wrap(~ Type))

drop

g.drop <- drop %>%
	ggplot(aes (x=Time, y=Kilobytes)) +
	geom_line(size=0.8)

# rtt = as_tibble(read.csv(sep=c('\t', ' '),"rtt_smallq.txt"))
# rtt2 <- gather(rtt, "type", "val", -segment)

(g.delay <- delay %>% #filter(Type=="LastDelay") %>%
	ggplot(aes(x=Time, y=DelayS*1000)) +
	geom_line(size=0.8) +
	ylab("RTT [s]") +
	xlab("Time [ms]")) 
	# geom_point(size=2) +

# delay
# g.cwnd <-  ggplot(data=cwnd, aes(x=time, y=cwndsize)) +
# 	geom_line() +
# 	geom_point(size=2) +
# 	ylab("Cwnd") +
# 	xlab("Time [s]") +
# 	scale_shape_manual(values=seq(0,10))
# # facet_grid(~ var)
# g.cwnd


# height = 2.7, width=4.35
ggsave("../plots/rates.pdf", g.rates, device=cairo_pdf)
ggsave("../plots/drop.pdf", g.drop, device=cairo_pdf)
ggsave("../plots/cwnd.pdf", g.cwnd, device=cairo_pdf)
ggsave("../plots/rtt.pdf", g.rtt, device=cairo_pdf)

