# Mike iLL PDF Book Tools

## Resources
https://github.com/AlexPof/mark2epub

### Following won't work on Intel Mac, requires

https://github.com/overcuriousity/pdf2epub

I can use [marker-pdf](https://github.com/VikParuchuri/marker) ([PyPi](https://pypi.org/project/marker-pdf/)) directly on Intel with following versions:
```
pdftext==0.3.7
torch==2.2.2
marker_pdf==0.2.6
```

Possibly I can use `marker_single input_file.pdf output_dir`, however a file of size `6.2M` took 30 minutes _and_ then errored out:
```
Traceback (most recent call last):
  File "/Volumes/Oggun/PDF books/bin/marker_single", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/convert_single.py", line 26, in main
    full_text, images, out_meta = convert_single_pdf(fname, model_lst, max_pages=args.max_pages, langs=langs, batch_multiplier=args.batch_multiplier)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/marker/convert.py", line 82, in convert_single_pdf
    pages, ocr_stats = run_ocr(doc, pages, langs, ocr_model, batch_multiplier=batch_multiplier)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/marker/ocr/recognition.py", line 57, in run_ocr
    new_pages = surya_recognition(doc, ocr_idxs, langs, rec_model, pages, batch_multiplier=batch_multiplier)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/marker/ocr/recognition.py", line 85, in surya_recognition
    results = run_recognition(images, surya_langs, rec_model, processor, polygons=polygons, batch_size=get_batch_size() * batch_multiplier)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/surya/ocr.py", line 31, in run_recognition
    rec_predictions, _ = batch_recognition(all_slices, all_langs, rec_model, rec_processor, batch_size=batch_size)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/surya/recognition.py", line 50, in batch_recognition
    return_dict = model.generate(
                  ^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/generation/utils.py", line 1593, in generate
    model_kwargs = self._prepare_encoder_decoder_kwargs_for_generation(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/generation/utils.py", line 742, in _prepare_encoder_decoder_kwargs_for_generation
    model_kwargs["encoder_outputs"]: ModelOutput = encoder(**encoder_kwargs)
                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/models/donut/modeling_donut_swin.py", line 925, in forward
    encoder_outputs = self.encoder(
                      ^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/models/donut/modeling_donut_swin.py", line 756, in forward
    layer_outputs = layer_module(
                    ^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/models/donut/modeling_donut_swin.py", line 680, in forward
    layer_outputs = layer_module(
                    ^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/models/donut/modeling_donut_swin.py", line 634, in forward
    layer_output = self.intermediate(layer_output)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/transformers/models/donut/modeling_donut_swin.py", line 499, in forward
    hidden_states = self.dense(hidden_states)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Volumes/Oggun/PDF books/lib/python3.12/site-packages/torch/nn/modules/linear.py", line 116, in forward
    return F.linear(input, self.weight, self.bias)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: MPS backend out of memory (MPS allocated: 2.56 GB, other allocations: 3.72 GB, max allowed: 6.80 GB). Tried to allocate 686.00 MB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
```

### Plugins Resource Repo
[https://github.com/RiccardoSilva42/Kobo-Hacks-Comp](https://github.com/RiccardoSilva42/Kobo-Hacks-Comp)
