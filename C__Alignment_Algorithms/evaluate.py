def evaluate(gold_src, gold_tgt, out_complex, out_simpl, without_identical=False):
	correct, n_out, n_gold = get_num_correct_aligns(gold_src, gold_tgt,
													out_complex, out_simpl, without_identical=without_identical)

	precision = correct / n_out
	recall = correct / n_gold

	if (precision + recall) > 0:
	    f1 = (2 * precision * recall) / (precision + recall)
	else:
	    f1 = 0

	return precision, recall, n_gold, n_out, correct, f1


def get_num_correct_aligns(gold_src, gold_tgt, out_complex, out_simpl, without_identical=False):
	with open(gold_src, 'r') as gold_src_file:
		gold_complex_sents = gold_src_file.readlines()

	with open(gold_tgt, 'r') as gold_tgt_file:
		gold_simpl_sents = gold_tgt_file.readlines()

	gold_complex_sents_cln = []
	for lin in gold_complex_sents:
		if '.eoa' in lin:
			pass
		else:
			gold_complex_sents_cln.append(lin.replace('.eoa', '').strip())

	gold_simpl_sents_cln = []
	for lin in gold_simpl_sents:
		if '.eoa' in lin:
			pass
		else:
			gold_simpl_sents_cln.append(lin.replace('.eoa', '').strip())

	if len(gold_simpl_sents_cln) != len(gold_complex_sents_cln):
		raise ValueError("Wrong input, gold files have different length of content.")

	with open(out_complex, 'r') as out_complex_file:
		out_complex_sents = out_complex_file.readlines()

	with open(out_simpl, 'r') as out_simpl_file:
		out_simpl_sents = out_simpl_file.readlines()

	out_complex_sents_cln = []
	for lin in out_complex_sents:
		if '.eoa' in lin:
			pass
		else:
			out_complex_sents_cln.append(lin.replace('.eoa', '').strip())

	out_simpl_sents_cln = []
	for lin in out_simpl_sents:
		if '.eoa' in lin:
			pass
		else:
			out_simpl_sents_cln.append(lin.replace('.eoa', '').strip())

	if len(out_complex_sents_cln) != len(out_simpl_sents_cln):
		raise ValueError("Wrong input, output files have different length of content.")

	golds = list(zip(gold_complex_sents_cln, gold_simpl_sents_cln))
	# if len(gold_complex_sents_cln) != len(golds.keys()):
	# 	print("gold complex:", len(gold_complex_sents_cln), "dictionary:", len(golds.keys()))
	# 	raise KeyError("Problem with method, dictionary has different size than input.")
	correct = 0
	aligned = len(out_complex_sents_cln)
	gold_aligned = len(gold_complex_sents_cln)
	if without_identical:
		for gold_complex, gold_simple in zip(gold_complex_sents_cln, gold_simpl_sents_cln):
			if gold_complex == gold_simple:
				gold_aligned -= 1

	for out_cmplx, out_simpl in zip(out_complex_sents_cln, out_simpl_sents_cln):
		if without_identical and out_cmplx == out_simpl:
			aligned -= 1
			continue
		if (out_cmplx, out_simpl) in golds:
			# print(out_simpl, '-----------', golds[out_cmplx])
			#if out_simpl == golds[out_cmplx]:
				# print(out_simpl, '-----------', golds[out_cmplx])
			correct += 1

	return correct, aligned, gold_aligned
	
	

# print("MASSalign without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/MASSalign/massalign_default.complex", "outputs/MASSalign/massalign_default.simple", without_identical=True))
print("MASSalign with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/MASSalign/massalign_default.complex", "outputs/MASSalign/massalign_default.simple", without_identical=False))


# print("CATS without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/CATS/CNG_3_closestSimStrategy_sentence_complex.txt", "outputs/CATS/CNG_3_closestSimStrategy_sentence_simple.txt", without_identical=True))
print("CATS with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/CATS/CNG_3_closestSimStrategy_sentence_complex.txt", "outputs/CATS/CNG_3_closestSimStrategy_sentence_simple.txt", without_identical=False))

# print("BERTalign without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/BERTalign/bertalign_alignments_default_params_trial_3.complex", "outputs/BERTalign/bertalign_alignments_default_params_trial_3.simple", without_identical=True))
print("BERTalign with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/BERTalign/bertalign_alignments_default_params_trial_3.complex", "outputs/BERTalign/bertalign_alignments_default_params_trial_3.simple", without_identical=False))

"""# print("LHA without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/LHA/x.complex", "outputs/LHA/x.simple", without_identical=True))
print("LHA with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/LHA/x.complex", "outputs/LHA/x.simple", without_identical=False))"""

# print("Sent-LaBSE without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/Sent-LaBSE/model_LaBSE_th_0.9_1_1.complex", "outputs/Sent-LaBSE/model_LaBSE_th_0.9_1_1.simple", without_identical=True))
print("Sent-LaBSE with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/Sent-LaBSE/model_LaBSE_th_0.9_1_1.complex", "outputs/Sent-LaBSE/model_LaBSE_th_0.9_1_1.simple", without_identical=False))

# print("Sent-RoBERTa without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/Sent-RoBERTa/model_cross-en-de-roberta_th_0.9_1_1.complex", "outputs/Sent-RoBERTa/model_cross-en-de-roberta_th_0.9_1_1.simple", without_identical=True))
print("Sent-RoBERTa with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/Sent-RoBERTa/model_cross-en-de-roberta_th_0.9_1_1.complex", "outputs/Sent-RoBERTa/model_cross-en-de-roberta_th_0.9_1_1.simple", without_identical=False))

# print("VecAlign without identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/VecAlign/test4_Vecalign_alignments.complex", "outputs/Sent-LaBSE/test4_Vecalign_alignments.simple", without_identical=True))
print("VecAlign with identicals", evaluate("DEplain_web_alignments_test.src", "DEplain_web_alignments_test.tgt", "outputs/VecAlign/test4_Vecalign_alignments.complex", "outputs/VecAlign/test4_Vecalign_alignments.simple", without_identical=False))










